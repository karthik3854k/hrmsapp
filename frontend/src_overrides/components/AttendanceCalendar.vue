<template>
	<div class="flex flex-col w-full gap-3" v-if="calendarEvents.data">
		<div class="text-base sm:text-lg text-white font-bold tracking-tight px-1">
			{{ __("Attendance Calendar") }}
		</div>

		<div class="flex flex-col gap-5 bg-[#07252c] py-5 px-3.5 sm:px-5 rounded-2xl shadow-xl border border-[#D4AF37]/35 text-white">
			<!-- Month Change -->
			<div class="flex flex-row justify-between items-center px-1">
				<Button
					icon="chevron-left"
					variant="ghost"
					class="!text-[#D4AF37] hover:!bg-white/10 !p-1.5 rounded-lg"
					@click="firstOfMonth = firstOfMonth.subtract(1, 'M')"
				/>
				<span class="text-base sm:text-lg text-white font-bold tracking-wide">
					{{ firstOfMonth.format("MMMM") }} {{ firstOfMonth.format("YYYY") }}
				</span>
				<Button
					icon="chevron-right"
					variant="ghost"
					class="!text-[#D4AF37] hover:!bg-white/10 !p-1.5 rounded-lg"
					@click="firstOfMonth = firstOfMonth.add(1, 'M')"
				/>
			</div>

			<!-- Calendar Grid -->
			<div class="grid grid-cols-7 gap-y-2 gap-x-1 sm:gap-x-2">
				<!-- Day Headers (S M T W T F S) -->
				<div
					v-for="day in DAYS"
					:key="day"
					class="flex justify-center text-slate-300 text-xs sm:text-sm font-semibold pb-1"
				>
					{{ day }}
				</div>

				<!-- Empty slots before 1st of month -->
				<div v-for="_ in firstOfMonth.get('d')" :key="'empty-' + _" />

				<!-- Days of the month -->
				<div
					v-for="index in firstOfMonth.endOf('M').get('D')"
					:key="'day-' + index"
					class="flex justify-center items-center"
				>
					<div
						class="w-full max-w-[42px] sm:max-w-[46px] min-h-[46px] py-1 px-0.5 rounded-xl flex flex-col items-center justify-between transition-all"
						:style="getDayTileStyle(index)"
					>
						<!-- Date Number -->
						<span
							class="text-xs sm:text-sm font-semibold leading-tight"
							:style="{ color: isToday(index) && !getDayStatus(index) ? '#D4AF37' : '#ffffff' }"
						>
							{{ index }}
						</span>

						<!-- Status letter below date -->
						<span
							v-if="getDayStatus(index)"
							class="text-[9px] sm:text-[10px] font-extrabold tracking-wider leading-none"
							:style="{ color: statusMap[getDayStatus(index)]?.color }"
						>
							{{ statusMap[getDayStatus(index)]?.code }}
						</span>
						<span v-else class="h-[9px] sm:h-[10px]"></span>
					</div>
				</div>
			</div>

			<!-- Divider -->
			<div class="w-full h-px bg-[#D4AF37]/20 my-1"></div>

			<!-- Summary -->
			<div class="grid grid-cols-4 gap-2 pt-1">
				<div
					v-for="status in summaryStatuses"
					:key="status"
					class="flex flex-col items-center gap-1.5 text-center"
				>
					<div class="flex flex-row gap-1.5 items-center justify-center">
						<span
							class="w-2.5 h-2.5 rounded-full shrink-0"
							:style="{ backgroundColor: statusMap[status]?.dot }"
						/>
						<span class="text-slate-300 text-[11px] sm:text-xs font-medium leading-none whitespace-nowrap">
							{{ __(status) }}
						</span>
					</div>
					<span class="text-white text-base sm:text-lg font-bold leading-tight">
						{{ summary[status] || 0 }}
					</span>
				</div>
			</div>
		</div>
	</div>
</template>

<script setup>
import { computed, inject, ref, watch } from "vue"
import { createResource, Button } from "frappe-ui"

const dayjs = inject("$dayjs")
const employee = inject("$employee")
const __ = inject("$translate")
const firstOfMonth = ref(dayjs().date(1).startOf("D"))

const statusMap = {
	Present: {
		code: "P",
		bg: "rgba(16, 185, 129, 0.22)",
		border: "1px solid rgba(16, 185, 129, 0.5)",
		color: "#34d399",
		dot: "#10b981",
	},
	"Work From Home": {
		code: "P",
		bg: "rgba(16, 185, 129, 0.22)",
		border: "1px solid rgba(16, 185, 129, 0.5)",
		color: "#34d399",
		dot: "#10b981",
	},
	"Half Day": {
		code: "HD",
		bg: "rgba(245, 158, 11, 0.22)",
		border: "1px solid rgba(245, 158, 11, 0.5)",
		color: "#fbbf24",
		dot: "#f59e0b",
	},
	Absent: {
		code: "A",
		bg: "rgba(239, 68, 68, 0.25)",
		border: "1px solid rgba(239, 68, 68, 0.55)",
		color: "#f87171",
		dot: "#ef4444",
	},
	"On Leave": {
		code: "L",
		bg: "rgba(59, 130, 246, 0.25)",
		border: "1px solid rgba(59, 130, 246, 0.55)",
		color: "#60a5fa",
		dot: "#3b82f6",
	},
	Holiday: {
		code: "H",
		bg: "rgba(148, 163, 184, 0.15)",
		border: "1px solid rgba(148, 163, 184, 0.35)",
		color: "#94a3b8",
		dot: "#64748b",
	},
}

const summaryStatuses = ["Present", "Half Day", "Absent", "On Leave"]

const summary = computed(() => {
	const summary = {}

	if (!calendarEvents.data) return summary

	for (const status of Object.values(calendarEvents.data)) {
		let updatedStatus = status === "Work From Home" ? "Present" : status
		if (updatedStatus in summary) {
			summary[updatedStatus] += 1
		} else {
			summary[updatedStatus] = 1
		}
	}

	return summary
})

watch(
	() => firstOfMonth.value,
	() => {
		calendarEvents.fetch()
	}
)

const getEventOnDate = (date) => {
	if (!calendarEvents.data) return null
	return calendarEvents.data[firstOfMonth.value.date(date).format("YYYY-MM-DD")]
}

const getDayStatus = (date) => {
	const ev = getEventOnDate(date)
	if (!ev) return null
	return ev
}

const isToday = (date) => {
	return firstOfMonth.value.date(date).isSame(dayjs(), "day")
}

const getDayTileStyle = (date) => {
	const status = getDayStatus(date)
	if (status && statusMap[status]) {
		return {
			backgroundColor: statusMap[status].bg,
			border: statusMap[status].border,
		}
	}

	if (isToday(date)) {
		return {
			backgroundColor: "rgba(212, 175, 55, 0.15)",
			border: "1px solid rgba(212, 175, 55, 0.6)",
		}
	}

	return {
		backgroundColor: "transparent",
		border: "1px solid transparent",
	}
}

const getFirstLetter = (s) => Array.from((s || "").trim())[0]

const DAYS = [
	getFirstLetter(__("Sunday")),
	getFirstLetter(__("Monday")),
	getFirstLetter(__("Tuesday")),
	getFirstLetter(__("Wednesday")),
	getFirstLetter(__("Thursday")),
	getFirstLetter(__("Friday")),
	getFirstLetter(__("Saturday")),
]

// resources
const calendarEvents = createResource({
	url: "hrms.api.get_attendance_calendar_events",
	auto: true,
	cache: "hrms:attendance_calendar_events",
	makeParams() {
		return {
			employee: employee.data?.name,
			from_date: firstOfMonth.value.format("YYYY-MM-DD"),
			to_date: firstOfMonth.value.endOf("M").format("YYYY-MM-DD"),
		}
	},
})
</script>
