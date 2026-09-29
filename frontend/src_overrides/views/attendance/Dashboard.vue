<template>
	<BaseLayout pageTitle="Attendance">
		<template #body>
			<div class="flex flex-col mt-5 mb-7 p-4 gap-6">
				<AttendanceCalendar />

				<div class="w-full">
					<router-link :to="{ name: 'AttendanceRequestFormView' }" v-slot="{ navigate }">
						<Button 
							@click="navigate" 
							variant="solid" 
							class="w-full py-4 text-base !bg-[#D4AF37] !text-[#051E24] !font-bold rounded-xl shadow-lg border-none hover:!bg-amber-400 transition cursor-pointer"
							style="background: linear-gradient(135deg, #E6CA65 0%, #D4AF37 50%, #B8860B 100%); color: #051E24;"
						>
							<template #prefix>
								<FeatherIcon name="plus-circle" class="w-5 h-5 mr-1" />
							</template>
							{{ __("Request Attendance") }}
						</Button>
					</router-link>
				</div>

				<div>
					<div class="text-base sm:text-lg text-white font-bold mb-1 tracking-tight px-1">{{ __("Recent Attendance Requests") }}</div>
					<RequestList
						:component="markRaw(AttendanceRequestItem)"
						:items="myAttendanceRequests?.data?.slice(0, 5)"
						:addListButton="true"
						:listButtonRoute="__('AttendanceRequestListView')"
					/>
				</div>

				<div>
					<div class="text-base sm:text-lg text-white font-bold mb-1 tracking-tight px-1">{{ __("Upcoming Shifts") }}</div>
					<RequestList
						:component="markRaw(ShiftAssignmentItem)"
						:items="upcomingShifts"
						:addListButton="true"
						listButtonRoute="ShiftAssignmentListView"
						:emptyStateMessage="__('You have no upcoming shifts')"
					/>
				</div>

				<div class="w-full">
					<router-link :to="{ name: 'ShiftRequestFormView' }" v-slot="{ navigate }">
						<Button 
							@click="navigate" 
							variant="solid" 
							class="w-full py-4 text-base !bg-[#D4AF37] !text-[#051E24] !font-bold rounded-xl shadow-lg border-none hover:!bg-amber-400 transition cursor-pointer"
							style="background: linear-gradient(135deg, #E6CA65 0%, #D4AF37 50%, #B8860B 100%); color: #051E24;"
						>
							<template #prefix>
								<FeatherIcon name="plus-circle" class="w-5 h-5 mr-1" />
							</template>
							{{ __("Request a Shift") }}
						</Button>
					</router-link>
				</div>

				<div>
					<div class="text-base sm:text-lg text-white font-bold mb-1 tracking-tight px-1">{{ __("Recent Shift Requests") }}</div>
					<RequestList
						:component="markRaw(ShiftRequestItem)"
						:items="myShiftRequests?.data?.slice(0, 5)"
						:addListButton="true"
						listButtonRoute="ShiftRequestListView"
					/>
				</div>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import { computed, inject, markRaw } from "vue"
import { createResource, Button, FeatherIcon } from "frappe-ui"

import BaseLayout from "@/components/BaseLayout.vue"
import AttendanceRequestItem from "@/components/AttendanceRequestItem.vue"
import ShiftRequestItem from "@/components/ShiftRequestItem.vue"
import ShiftAssignmentItem from "@/components/ShiftAssignmentItem.vue"
import RequestList from "@/components/RequestList.vue"
import AttendanceCalendar from "@/components/AttendanceCalendar.vue"

import {
	getShiftDates,
	getTotalShiftDays,
	getShiftTiming,
	myAttendanceRequests,
	myShiftRequests,
} from "@/data/attendance"

const employee = inject("$employee")
const dayjs = inject("$dayjs")
const __ = inject("$translate")

const shifts = createResource({
	url: "hrms.api.get_shifts",
	auto: true,
	cache: "hrms:shifts",
	makeParams() {
		return {
			employee: employee.data?.name,
		}
	},
	transform: (data) => {
		return data.map((assignment) => {
			assignment.doctype = "Shift Assignment"
			assignment.is_upcoming = !assignment.end_date || dayjs(assignment.end_date).isAfter(dayjs())
			assignment.shift_dates = getShiftDates(assignment)
			assignment.total_shift_days = getTotalShiftDays(assignment)
			assignment.shift_timing = getShiftTiming(assignment)
			return assignment
		})
	},
})

const upcomingShifts = computed(() => {
	const filteredShifts = shifts.data?.filter((shift) => shift.is_upcoming)

	// show only 5 upcoming shifts
	return filteredShifts?.slice(0, 5)
})
</script>
