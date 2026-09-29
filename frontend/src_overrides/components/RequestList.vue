<template>
	<div class="flex flex-col bg-white rounded-2xl shadow-sm border border-slate-100 mt-4 overflow-hidden divide-y divide-slate-100" v-if="props.items?.length">
		<div
			class="flex flex-row p-3.5 sm:p-4 items-center justify-between hover:bg-slate-50/80 active:bg-slate-100 transition cursor-pointer"
			v-for="link in props.items"
			:key="link.name"
			@click="openRequestModal(link)"
		>
			<component
				:is="props.component || link.component"
				:doc="link"
				:workflowStateField="link.workflow_state_field"
				:isTeamRequest="props.teamRequests"
			/>
		</div>

		<router-link
			v-if="props.addListButton"
			:to="{ name: props.listButtonRoute }"
			v-slot="{ navigate }"
		>
			<Button
				variant="ghost"
				@click="navigate"
				class="w-full !text-amber-600 hover:!text-amber-700 font-semibold py-4 text-xs sm:text-sm border-none bg-white hover:bg-slate-50 transition"
			>
				{{ __("View List") }} &rarr;
			</Button>
		</router-link>
	</div>
	<EmptyState :message="emptyStateMessage || __('You have no requests')" v-else />

	<ion-modal
		ref="modal"
		:is-open="isRequestModalOpen"
		@didDismiss="closeRequestModal"
		:initial-breakpoint="1"
		:breakpoints="[0, 1]"
	>
		<RequestActionSheet :fields="fieldsMap[selectedRequest?.doctype]" v-model="selectedRequest" />
	</ion-modal>
</template>

<script setup>
import { ref, inject } from "vue"
import { IonModal } from "@ionic/vue"
import RequestActionSheet from "@/components/RequestActionSheet.vue"
import EmptyState from "@/components/EmptyState.vue"
import { Button } from "frappe-ui"

import {
	LEAVE_FIELDS,
	EXPENSE_CLAIM_FIELDS,
	ATTENDANCE_REQUEST_FIELDS,
	SHIFT_REQUEST_FIELDS,
	SHIFT_FIELDS,
} from "@/data/config/requestSummaryFields"

const __ = inject("$translate")
const props = defineProps({
	component: {
		type: Object,
		required: false,
	},
	items: {
		type: Array,
		required: true,
	},
	addListButton: {
		type: Boolean,
		required: false,
		default: false,
	},
	listButtonRoute: {
		type: String,
		required: false,
	},
	emptyStateMessage: {
		type: String,
		required: false,
	},
	teamRequests: {
		type: Boolean,
		required: false,
		default: false,
	},
})

const isRequestModalOpen = ref(false)
const selectedRequest = ref(null)

const fieldsMap = {
	"Leave Application": LEAVE_FIELDS,
	"Expense Claim": EXPENSE_CLAIM_FIELDS,
	"Attendance Request": ATTENDANCE_REQUEST_FIELDS,
	"Shift Request": SHIFT_REQUEST_FIELDS,
	"Shift Assignment": SHIFT_FIELDS,
}

function openRequestModal(request) {
	selectedRequest.value = request
	isRequestModalOpen.value = true
}

function closeRequestModal() {
	selectedRequest.value = null
	isRequestModalOpen.value = false
}
</script>
